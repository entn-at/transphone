from pathlib import Path
from transphone.config import TransphoneConfig
import shutil


def get_all_models(alt_model_path=None):
    """
    get all local models

    :return:
    """
    if alt_model_path:
        model_dir = alt_model_path
    else:
        model_dir = TransphoneConfig.data_path / 'model'

    models = list(sorted(model_dir.glob('*'), reverse=True))

    #assert len(models) > 0, "No models are available, you can maually download a model with download command or just run inference to download the latest one automatically"

    return models


def get_model_path(model_name, alt_model_path=None):
    """
    get model path by name, verify its a valid path

    :param model_name: str
    :return: model path
    """
    if alt_model_path:
        model_dir = alt_model_path
    else:
        model_dir = TransphoneConfig.data_path / 'model'

    resolved_model_name = resolve_model_name(model_name)

    assert resolved_model_name != "none", model_name+" is not a valid model name. please check by list_model"

    return model_dir / resolved_model_name


def copy_model(src_model_name, tgt_model_name):
    """
    copy a model to a new model

    :param src_model_name:
    :param tgt_model_name:
    :return:
    """

    # verify the source path is not empty
    src_model_path = get_model_path(src_model_name)

    # verify the target path is empty
    model_dir = Path(__file__).parent / 'pretrained' / 'model'
    tgt_model_path = model_dir / tgt_model_name

    assert not tgt_model_path.exists(), \
        "provided model name "+tgt_model_name+" has already exist. Consider another name or delete the existing one"

    shutil.copytree(str(src_model_path), str(tgt_model_path))


def delete_model(model_name):

    model_path = get_model_path(model_name)

    answer = input(f"you will delete {model_path}? [Y|N]")
    if answer.lower() in ['y', 'yes', 'true']:
        print("deleting ", model_path)
        shutil.rmtree(str(model_path))


def resolve_model_name(model_name='latest', alt_model_path=None):
    """
    select the model

    :param model_name:
    :return:
    """

    models = get_all_models(alt_model_path)

    # match model name
    for model in models:
        if model.name == model_name:
            return model_name

    # get the latest model in local
    if model_name == 'latest':
        return models[0].name

    return "none"