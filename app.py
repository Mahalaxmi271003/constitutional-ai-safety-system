import streamlit as st

from src.safety_pipeline import ConstitutionalAISafetySystem


st.set_page_config(
    page_title="Constitutional AI Safety System",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Constitutional AI Safety System")

st.write(
    "A GPT-2 generation pipeline combined with a BERT-based "
    "safety evaluator and automated response retry mechanism."
)

st.divider()

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Explain artificial intelligence in simple terms.",
    height=120
)

if st.button("Generate Safe Response", type="primary"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:

        with st.spinner("Generating and evaluating response..."):

            system = ConstitutionalAISafetySystem(max_retries=3)
            result = system.generate_safe_response(prompt)

        st.subheader("Final Response")

        st.write(result["final_response"])

        st.divider()

        if result["status"] == "SAFE":
            st.success("✓ Response passed the safety evaluation.")
        else:
            st.warning("⚠ Response requires review.")

        st.write(
            f"**Generation attempts:** "
            f"{len(result['attempts'])}"
        )

        with st.expander("View evaluation details"):

            for attempt in result["attempts"]:

                st.write(
                    f"### Attempt {attempt['attempt']}"
                )

                st.write(attempt["response"])

                evaluation = attempt["evaluation"]

                st.write(
                    f"Label: `{evaluation['label']}`"
                )

                st.write(
                    f"Confidence: `{evaluation['score']}`"
                )

                st.write(
                    f"Safe: `{evaluation['is_safe']}`"
                )