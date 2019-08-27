import pytest

from vtools.evaluate import site_concordancy

from cyvcf2 import VCF


@pytest.fixture(scope='module')
def known_concordant():
    filename = 'tests/cases/gatk.vcf.gz'
    call = VCF(filename, gts012=True)
    positive = VCF(filename, gts012=True)
    d, disc = site_concordancy(call, positive, call_samples=['NA12878'],
                               positive_samples=['NA12878'],
                               min_gq=0, min_dp=0)
    return d


def test_total_sites(known_concordant):
    assert known_concordant['total_sites'] == 37


def test_sites_considered(known_concordant):
    assert known_concordant['sites_considered'] == 37


def test_alleles_considered(known_concordant):
    assert known_concordant['alleles_considered'] == 74


def test_alleles_het_concordant(known_concordant):
    assert known_concordant['alleles_het_concordant'] == 42


def test_alleles_hom_alt_concordant(known_concordant):
    assert known_concordant['alleles_hom_alt_concordant'] == 18


def test_alleles_hom_ref_concordant(known_concordant):
    assert known_concordant['alleles_hom_ref_concordant'] == 14


def test_alleles_concordant(known_concordant):
    assert known_concordant['alleles_concordant'] == 74


def test_alleles_discordant(known_concordant):
    assert known_concordant['alleles_discordant'] == 0


def test_alleles_no_call(known_concordant):
    assert known_concordant['alleles_no_call'] == 0


def test_alleles_low_qual(known_concordant):
    assert known_concordant['alleles_low_qual'] == 0


def test_alleles_low_depth(known_concordant):
    assert known_concordant['alleles_low_depth'] == 0


@pytest.fixture(scope='module')
def BLANK_NA12878():
    filename = 'tests/cases/gatk.vcf.gz'
    call = VCF(filename, gts012=True)
    positive = VCF(filename, gts012=True)
    d, disc = site_concordancy(call, positive, call_samples=['BLANK'],
                               positive_samples=['NA12878'],
                               min_gq=30, min_dp=20)
    return d


def test_low_qual_30(BLANK_NA12878):
    assert BLANK_NA12878['alleles_low_qual'] == 42


def test_low_depth_20(BLANK_NA12878):
    assert BLANK_NA12878['alleles_low_depth'] == 44


def test_no_call(BLANK_NA12878):
    assert BLANK_NA12878['alleles_no_call'] == 8


@pytest.fixture(scope='module')
def NA12878_BLANK():
    filename = 'tests/cases/gatk.vcf.gz'
    call = VCF(filename, gts012=True)
    positive = VCF(filename, gts012=True)
    d, disc = site_concordancy(call, positive, call_samples=['NA12878'],
                               positive_samples=['BLANK'],
                               min_gq=30, min_dp=20)
    return d


# def test_no_call2(NA12878_BLANK):
#     assert NA12878_BLANK['alleles_no_call'] == 8
