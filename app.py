import streamlit as st 
import requests

key=st.secrets["OPENROUTER_API_KEY"]

st.title("Code Generator")

prompt=st.text_area("Enter your prompt")
language=st.selectbox("Select Language",["python","c","c++","java"])

if st.button("Generate Code"):

    if prompt:
        with st.spinner("Generating Code..."):

            url = "https://openrouter.ai/api/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }

            body = {
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Generate beginner-friendly code in {language}. Requirement: {prompt}"
                    }
                ]
            }

            try:
                response = requests.post(
                    url,
                    headers=headers,
                    json=body,
                    timeout=60
                )

                response.raise_for_status()

                result = response.json()

                code = result["choices"][0]["message"]["content"]

                st.success("Code Generated Successfully!")
                st.code(code, language=language)

            except requests.RequestException as e:
                st.error(f"API Error: {e}")

            except (KeyError, IndexError):
                st.error("Invalid API response.")

    else:
        st.warning("Please enter your prompt.")
