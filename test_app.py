from app import app


# This test suite checks if the basic UI elements are rendered correctly
def test_header_exists(dash_duo):
    # Start the app
    dash_duo.start_server(app)

    # 1. Check if the header is present by its ID
    # 'wait_for_element' is better than 'find_element' because it accounts for loading time
    header = dash_duo.wait_for_element("#header")

    assert header is not None
    assert header.text == "Pink Morsel Sales Visualizer"


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)

    # 2. Check if the graph is present
    visualization = dash_duo.wait_for_element("#sales-line-chart")

    assert visualization is not None


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)

    # 3. Check if the radio buttons (region picker) are present
    region_picker = dash_duo.wait_for_element("#region-filter")

    assert region_picker is not None