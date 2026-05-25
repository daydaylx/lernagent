import importlib


def test_app_modules_importable() -> None:
    modules = [
        "app.config",
        "app.scanner",
        "app.cache",
        "app.indexer",
        "app.explainer",
        "app.ai_client",
        "app.ui",
    ]
    for mod in modules:
        assert importlib.import_module(mod) is not None
