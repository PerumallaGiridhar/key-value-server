from uuid import UUID
from logger import get_logger

logger = get_logger('file-loader')

def get_lookup_data(filepath):
    """
    loading data and creating a lookup dictionary
    """
    logger.info("Reading file content on path %s", filepath)
    with open(filepath, 'r') as f:
        data = f.readlines()
    logger.info("Preparing data for lookup of length %s", str(len(data)))
    lookup = {
        UUID(uuid_str): rest
        for row in data
        if (split_row := row.split(" ", 1))
        and (uuid_str := split_row[0])
        and (rest := split_row[1].strip())
    }
    logger.info("Loading file data completed with %s items", len(lookup))
    return lookup
