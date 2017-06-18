from viewers.console import ConsoleViewer
from controllers.flowers_controller import FlowersController
from utils import config

conf = config.Configuration()
config.Configuration = conf

viewer = ConsoleViewer()
controller = FlowersController()
controller.parse_all_sites()
controller.view_data(viewer)
