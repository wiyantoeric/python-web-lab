import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure as fg
import pydeck as pdk
import graphviz
import time

st.set_page_config(page_title="Streamlit components")

with st.expander("#1 Write and magic"):
    # Write
    st.write("Hello, world!")
    # Magic
    arr = np.random.normal(1, 1, size=100)
    arr

with st.expander("#2 Text elements"):
    st.markdown("Streamlit is awesome! [Learn more about it](https://streamlit.io)")
    st.title("Let's dig into text elements in Streamlit")
    st.subheader("And this is a subheader")
    st.caption("What about a caption?")
    st.code("""# Show codes with st.code()
    def greet():
        print('Hello!')""", language="python")
    st.text("This is st.text()")
    st.latex(r'''
        e = m c^2
        ''')

with st.expander("#3 Data display elements"):
    numbers = np.array([i*0.1 + np.random.randn() for i in range (3)])
    df = pd.DataFrame(
            numbers,
            columns=['Random Value'],
            dtype=float,
        )
    st.dataframe(data=df, use_container_width=True)

    st.table(data=df)
    st.metric(label="Value count", value="3 row")
    st.json({
        'value_count': '3 row',
        'dtype': 'float',
    })

with st.expander("#4 Chart elements"):
    data_count = 100
    random_data = np.array([i*0.1 + np.random.randn() for i in range (data_count)])

    chart_data = pd.DataFrame(
            random_data,
            columns=['Random Value'],
            dtype=float,
        )
    
    st.write("Line chart")
    st.line_chart(chart_data)
    
    st.write("Area chart")
    st.area_chart(chart_data)
    
    st.write("Bar chart")
    st.bar_chart(chart_data)
    
    st.write("Pyplot")

    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    
    st.pyplot(fig)
    
    st.write('Altair chart')
    df2 = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
    }, columns=['x', 'y'])

    df3 = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'z': np.random.randn(100),
    })

    chart = alt.Chart(df2).mark_point().encode(
        x='x',
        y='y',
        color=alt.value('steelblue'),
        tooltip=['x', 'y']
    )

    st.altair_chart(df2, use_container_width=True)

    st.write('Vega lite chart')
    st.vega_lite_chart(df2, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'x', 'type': 'quantitative'},
            'y': {'field': 'y', 'type': 'quantitative'},
            'size': {'field': 'y', 'type': 'quantitative'},
            'color': {'field': 'y', 'type': 'quantitative'},
        },
    })
    
    st.write('Plotly chart')
    x = np.random.randn(100)
    y = np.random.randn(100)

    hist_data = [x, y]

    group_labels = ['X', 'Y']

    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .1])

    st.plotly_chart(fig, use_container_width=True)

    st.write('Bokeh chart')

    bokeh_value1 = [1,2,3,4,5]
    bokeh_value2 = [1,4,9,16,25]
    
    p = fg(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')

    p.line(bokeh_value1, bokeh_value2, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)
    
    st.write('Pydeck chart')

    lat = 0.7893
    lon = 113.9213

    chart_data = pd.DataFrame(np.random.randn(2000, 2) / [15, 15] + [lat, lon], columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=9,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=300,
            ),
        ],
    ))

    st.write('Graphviz chart')

    graph = graphviz.Digraph()
    graph.edge('start', 'update')
    graph.edge('update', 'loading')
    graph.edge('loading', 'execute')
    graph.edge('execute', 'terminate')
    graph.edge('terminate', 'start')

    st.graphviz_chart(graph)

    st.write('Map')
    df = pd.DataFrame(np.random.randn(2000, 2) / [15, 15] + [lat, -lon], columns=['lat', 'lon'])

    st.map(df)

with st.expander("#5 Input widgets"):
    button = st.button('Give me ballon')
    
    if (button):
        st.balloons()
    
    st.write('Experimental data editor')
    st.experimental_data_editor(df)

    st.write('Download button')
    st.download_button('Download text', 'Lorem ipsum')
    
    st.write('Checkbox')
    st.write('And logic operation')
    op1 = st.checkbox('A')
    op2 = st.checkbox('B')

    if (op1 and op2):
        st.write('Voila!')
    
    st.write('Radio')
    radio = st.radio("What's your first programming language?", ('C++','Java','Python'))
    if (radio):
        st.write(f"Cool! I've tried {radio} too")
    
    st.write('Selectbox')
    st.selectbox('What\'s your field of interest?', ('Software Engineering', 'UX Designer', 'Other'))
    
    st.write('Multiselect')
    multiselect = st.multiselect('Programming language you liked',
    ['Python', 'Javascript', 'Java', 'C++', 'Dart', 'Go', 'Rust', 'PHP', 'R', 'C#', 'C'])
    
    st.write('Slider')
    st.slider(
    f"How much do you like {radio} as your first programming language?",
    0.0, 100.0)
    
    st.write('Select slider')
    low_like, high_like = st.select_slider(
        f"How much do you like {radio} as your first programming language?",
        options=[0, 10, 25, 50, 75, 90, 100],
        value=(10, 50)
    )
    st.write(f"You like it from the scale of {low_like} to {high_like}")
    
    st.write('Text input')
    st.text_input(f"How do you think {radio} improve your knowledge in programming?")
    
    st.write('Number input')
    st.number_input(f"Great! How much do you recommend {radio} to other?")
    
    st.write('Text area')
    st.text_area(f"What did you learn best from {radio}?")
    
    st.write('Date input')
    st.date_input("When did you start your college?")
    
    st.write('Time input')
    st.time_input("When is your coding time?")
    
    st.write('File uploader')
    image = st.file_uploader("Any coding you like to share? (photo)")
    if (image):
        st.image(image)
    
    st.write('Camera input')
    st.camera_input("You can take a photo with this widget")
    
    st.write('Color picker')
    st.color_picker("What color do you like?")

with st.expander("#6 Media elements"):
    st.write("Image")
    st.image("https://source.unsplash.com/200x200")
    st.write("Audio")
    st.audio("https://cdn.pixabay.com/download/audio/2023/03/16/audio_df7d9198c3.mp3?filename=floating-abstract-142819.mp3&g-recaptcha-response=03AFY_a8W1yO4lX9zL8RDkrn5Y1hpGF1pItWPeAd4CnKmbIYJEsYmhkIEUERQaYI8ZZB6Pljq_psd8ozh-vyrap79B1uIGbUqteOPZU_vUZb1AOKGOnftmllmcTQTUOpo5qk9-dlhfmUQrivu6YDQeoKUa5LkCB2f0eYX7IN66Oj6SwjmuP4FEGy9BtfQ3TAyZKg5vL-jD6PKCNyAeJ3bxiU8uwJJUMBVYD6i14bkBvbNrL9jEMo6vdIVQNglhjoaKFgk4gc66zqCdwwfPq03R4Fl7jczxY1oXgJMUV4PM_uqxacYbsYcqYqkj3wBSJ_SQrFEtRVnKYSBG4ql4uAQmFBHd16CNGJZHuZ2hi3SOm7eGqbkvAOZShdS5tIzOQas7EY1mbI1dt3kXOkdkPtl5b7Eu2NviYYKMwYduHDTVdYGUNR2xVNqBIov-A6SMXnsgt0t39V8ijsz9LQ-JizLlthIwEHRK8FfCRBhRH2ZxejwhhqgvPcn-LtC8ZrZDBdhJFOGdCNM2WUXf&remote_template=1")
    st.write("Video")
    st.video("https://www.youtube.com/watch?v=5Ac941RYeKo")

with st.expander("#7 Layouts and containers"):
    st.write("Sidebar")
    st.sidebar.header("Eric Wiyanto")
    st.sidebar.caption("Streamlit widgets assignment")
    st.write("Columns")
    col1, col2 = st.columns([3, 1])
    col1.image("https://static.streamlit.io/examples/cat.jpg")
    col2.image("https://static.streamlit.io/examples/dog.jpg")
    st.write("Tabs")
    tab1, tab2, tab3 = st.tabs(["200", "300", "400"])

    with tab1:
        st.header("A cat")
        st.image("https://source.unsplash.com/200x200", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://source.unsplash.com/300x300", width=300)

    with tab3:
        st.header("An owl")
        st.image("https://source.unsplash.com/400x400", width=400)

    st.write("Container")
    container = st.container()
    container.write("Contained text")
    st.write("Empty")
    empty = st.empty()
    empty.text("Empty's text")

with st.expander("#8 Status elements"):
    st.write("Progress")
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1, text=progress_text)
    st.write("Spinner")
    with st.spinner():
        time.sleep(1)
    if(st.button("Tap for balloons")):
        st.balloons()
    if(st.button("Tap for snow")):
        st.snow()
    st.error("This is an error dialog")
    st.warning("This is a warning dialog")
    st.info("This is an info dialog")
    st.success("This is a success dialog")
    e = RuntimeError('This is a exception dialog')
    st.exception(e)

with st.expander("#10 Utilities"):
    # page config is placed at the first code line due to streamlit documentation
    if st.button("Echo"): st.echo("Hi")
    st.write("Help")
    st.help(st.button('Help : st.button() documentation'))
    st.write("Experimental show")
    st.experimental_show(df)
    # Experimental set query params
    st.experimental_set_query_params(my_github_username="wiyantoeric")
    st.write("Experimental get query params")
    st.write(st.experimental_get_query_params())
    
with st.expander("#9 Control flow"):
    st.write("Stop")
    fav_lang = st.text_input('Your favorite language')
    if not fav_lang:
        st.warning('It seems you haven\'t enter the text field')
        st.stop()
    with st.form("fav_lang_form"):
        st.write(f"How much are your statisfied with {fav_lang}?")
        slider_val = st.slider("Favourite meter", min_value=0, max_value=10, step=1)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Form submitted! You've just rated {fav_lang} with score ", slider_val)
    st.write("Experimental rerun")

    if(st.button("Click to reset page")): st.experimental_rerun()
