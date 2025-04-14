from lib import printMsg
from core.api import apiTest
import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__),'.')))
from helpdesk.api import apiTest as apitest2

printMsg() # same level
apiTest() # one level down.
print(apitest2())