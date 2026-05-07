import streamlit as st

st.markdown(
    """
    <style>
        /* Only apply these rules to screens wider than 768px (Desktops/Laptops) */
        @media (min-width: 768px) {
            /* Make the main content area wider */
            .block-container {
                max-width: 70%;
                padding-top: 2rem;
            }

            /* Make the Sidebar Logo larger */
            [data-testid="stSidebarHeader"] img {
                max-height: 100px;
                width: auto;
            }
        }
        
        /* Optional: CSS for all screens (Headers) */
        @import url('https://fonts.googleapis.com/css2?family=Darumadrop+One&display=swap');
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Darumadrop One', cursive;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Donate to SCLA")

st.text("In addition to joining SCLA, consider supporting the Association by making a special donation. Your donation supports librarians, library workers, and library supporters as they work to advocate for and improve library services in South Carolina. Thank you so much for your support of our libraries.")

st.link_button("Donate", "https://secure.moolahpaymentsgateway.com/cart/cart.php?action=show_information&internal_key=c4757cfe9a9dc983f065d7ec88656ff1&internal_timestamp=1778188773&tid=1ee2c9a233ec22698b1a7ef0181d38cf", type="primary")