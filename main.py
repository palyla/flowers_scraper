from viewers.excel import ExcelViewer
from viewers.console import ConsoleViewer
from controllers.flowers_controller import FlowersController
from utils import config

conf = config.Configuration()
config.Configuration = conf

controller = FlowersController()
controller.parse_all_sites()
controller.view_data(ConsoleViewer())
controller.view_data(ExcelViewer(conf.get('excel', 'path_to_excel')))
