# import logging
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')

# import logging
# logging.basicConfig(format='%(asctime)s - %(message)s',
#                     level=logging.INFO)
# logging.info('Admin logged in')

import logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S')
logging.warning('Admin logged out')


# import logging
# logging.basicConfig(format='%(asctime)s - %(message)s - %(levelno)s',
#                     level=logging.INFO)
# logging.info('Admin logged in')