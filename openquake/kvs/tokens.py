"""Tokens for kvs keys."""
import openquake.kvs

# hazard tokens
SOURCE_MODEL_TOKEN = 'sources'
GMPE_TOKEN = 'gmpe'
JOB_TOKEN = 'job'
ERF_KEY_TOKEN = 'erf'
MGM_KEY_TOKEN = 'mgm'
HAZARD_CURVE_KEY_TOKEN = 'hazard_curve'
MEAN_HAZARD_CURVE_KEY_TOKEN = 'mean_hazard_curve'
QUANTILE_HAZARD_CURVE_KEY_TOKEN = 'quantile_hazard_curve'
STOCHASTIC_SET_TOKEN = 'ses'
MEAN_HAZARD_MAP_KEY_TOKEN = 'mean_hazard_map'
QUANTILE_HAZARD_MAP_KEY_TOKEN = 'quantile_hazard_map'

# risk tokens
CONDITIONAL_LOSS_KEY_TOKEN = 'LOSS_AT_'
EXPOSURE_KEY_TOKEN = 'ASSET'
GMF_KEY_TOKEN = 'GMF'
LOSS_RATIO_CURVE_KEY_TOKEN = 'LOSS_RATIO_CURVE'
LOSS_CURVE_KEY_TOKEN = 'LOSS_CURVE'


def loss_token(poe):
    """ Return a loss token made up of the CONDITIONAL_LOSS_KEY_TOKEN and 
    the poe cast to a string """
    return "%s%s" % (CONDITIONAL_LOSS_KEY_TOKEN, str(poe))


def vuln_key(job_id):
    """Generate the key used to store vulnerability curves."""
    return openquake.kvs.generate_product_key(job_id, "VULN_CURVES")


def asset_key(job_id, row, col):
    """ Return an asset key generated by openquake.kvs._generate_key """
    return openquake.kvs.generate_key([job_id, row, col,
            EXPOSURE_KEY_TOKEN])


def loss_ratio_key(job_id, row, col, asset_id):
    """ Return a loss ratio key generated by openquake.kvs.generate_key """
    return openquake.kvs.generate_key([job_id, row, col,
            LOSS_RATIO_CURVE_KEY_TOKEN, asset_id])


def loss_curve_key(job_id, row, col, asset_id):
    """ Return a loss curve key generated by openquake.kvs.generate_key """
    return openquake.kvs.generate_key([job_id, row, col, 
            LOSS_CURVE_KEY_TOKEN, asset_id])


def loss_key(job_id, row, col, asset_id, poe):
    """ Return a loss key generated by openquake.kvs.generate_key """
    return openquake.kvs.generate_key([job_id, row, col, loss_token(poe),
            asset_id])


def mean_hazard_curve_key(job_id, site):
    """Return the key used to store a mean hazard curve
    for a single site."""
    return openquake.kvs.generate_key([MEAN_HAZARD_CURVE_KEY_TOKEN,
            job_id, site.longitude, site.latitude])


def quantile_hazard_curve_key(job_id, site, quantile):
    """Return the key used to store a quantile hazard curve
    for a single site."""
    return openquake.kvs.generate_key(
            [QUANTILE_HAZARD_CURVE_KEY_TOKEN,
            job_id, site.longitude, site.latitude,
            str(quantile)])


def mean_hazard_map_key(job_id, site, poe):
    """Return the key used to store the IML used in mean hazard
    maps for a single site."""
    return openquake.kvs.generate_key([MEAN_HAZARD_MAP_KEY_TOKEN,
            job_id, site.longitude, site.latitude,
            str(poe)])


def quantile_hazard_map_key(job_id, site, poe, quantile):
    """Return the key used to store the IML used in quantile
    hazard maps for a single site."""
    return openquake.kvs.generate_key([QUANTILE_HAZARD_MAP_KEY_TOKEN,
            job_id, site.longitude, site.latitude,
            str(poe), str(quantile)])


def hazard_curve_key(job_id, realization_num, site_lon, site_lat):
    """ Result a hazard curve key (for a single site) generated by
    openquake.kvs.generate_key """
    return openquake.kvs.generate_key([HAZARD_CURVE_KEY_TOKEN,
            job_id, realization_num, site_lon, site_lat])
