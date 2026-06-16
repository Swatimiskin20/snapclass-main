import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    join_url = (
        f"https://snapclass-main.streamlit.app/?join-code={subject_code}"
    )

    st.header(f"Join {subject_name}")

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Join Link", join_url)
        st.text_input("Class Code", subject_code)
        st.info("Copy this link to share via WhatsApp or email.")

    with col2:
        st.image(out.getvalue(), caption="QR Code for class joining")