from flask import Blueprint
from evertcore.plugins import connect_listener, AppPlugin
import pandas as pd
from evertcore.plugins import register_plugin_settings, get_plugin_settings
from evertcore.plugins import emit_feature_data, register_plugin
from .pca import apply_pca

__plugin__ = "PCA"
__plugin_type__ = 'add_on'

pca = Blueprint('pca', __name__)


def run_plugin(data):
    print('event_emitted')

    if not isinstance(data, pd.DataFrame):
        raise TypeError('Expected input of type: pandas.DataFrame for argument: data_before, instead got: {}'.
                        format(type(data)))

    data_after = apply_pca(data)
    # emit_feature_data(data_after, __plugin__)
    return


class PCA(AppPlugin):

    def setup(self):
        self.register_blueprint(pca)
        register_plugin(__plugin__, __plugin_type__)
        connect_listener("add_on_event", run_plugin)