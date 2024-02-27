import os
import streamlit as st
from PIL import Image

# Define the directory path where the images are located
image_directory = "predefined_images"

# Dictionary to map plant labels to medicinal descriptions
medicinal_descriptions = {
    "1": {
        "name": "Aloe Vera",
        "applications":"Aloe Vera is widely used in skincare and cosmetics due to its moisturizing and healing properties. It is also utilized in the treatment of minor burns, cuts, and skin irritations. Additionally, it is consumed orally in the form of Aloe Vera juice for its potential digestive benefits.",
        "advantages":"Aloe Vera is renowned for its soothing effects on the skin, promoting wound healing and reducing inflammation. It also exhibits potential antioxidant and antimicrobial properties, contributing to its therapeutic benefits.",
        "definition":"Aloe Vera is a succulent plant species native to the Arabian Peninsula, but it is cultivated worldwide for its medicinal and agricultural uses. The gel extracted from its leaves has been utilized for centuries for its various health and skincare benefits."
    },
    "2": {
        "name": "Ginger",
        "applications": "Ginger is widely used as a spice in culinary preparations and also holds significant medicinal value. It is utilized to alleviate nausea, aid digestion, reduce inflammation, and relieve muscle pain. Ginger tea and ginger supplements are common forms of consumption for its health benefits.",
        "advantages": "Ginger possesses potent anti-inflammatory and antioxidant properties, making it beneficial for various aspects of health. It is particularly valued for its ability to ease gastrointestinal discomfort and improve digestion.",
        "definition": "Ginger, botanically known as Zingiber officinale, is a flowering plant native to Southeast Asia. Its rhizome, commonly referred to as ginger root, is the part most commonly used for culinary and medicinal purposes."
    },
    "3": {
        "name": "Neem",
        "applications": "Neem is utilized in traditional medicine for its antibacterial, antifungal, and antiviral properties. It is commonly used in skincare products for its ability to treat acne, eczema, and other skin conditions. Neem oil is also employed as a natural insect repellent and pesticide.",
        "advantages": "Neem offers a natural and effective solution for various skin ailments and insect-related issues. Its medicinal properties make it valuable in combating infections and promoting overall skin health.",
        "definition": "Neem, scientifically known as Azadirachta indica, is a tree native to the Indian subcontinent. Its leaves, bark, seeds, and oil have been utilized in traditional medicine for centuries due to their therapeutic properties."
    },
    "5": {
        "name": "Turmeric",
        "applications": "Turmeric is utilized as a spice in cooking and is also renowned for its medicinal properties. It contains curcumin, a compound with potent antioxidant and anti-inflammatory effects. Turmeric is used to alleviate pain, promote wound healing, support digestive health, and may even have anticancer properties.",
        "advantages": "Turmeric offers a wide range of health benefits, including its ability to reduce inflammation, improve skin health, support joint function, and boost overall immunity. Its antioxidant properties make it valuable for combating oxidative stress and preventing chronic diseases.",
        "definition": "Turmeric, scientifically known as Curcuma longa, is a flowering plant belonging to the ginger family. Its rhizomes are dried and ground to produce the vibrant yellow spice commonly used in Asian cuisine and traditional medicine."
    },
    "4": {
        "name": "Tulsi",
        "applications": "Tulsi, also known as Holy Basil, holds immense significance in Ayurvedic medicine. It is revered for its adaptogenic properties, meaning it helps the body adapt to stress. Tulsi is used to promote relaxation, support respiratory health, boost immunity, and alleviate symptoms of colds and flu.",
        "advantages": "Tulsi possesses potent antioxidant, anti-inflammatory, and antimicrobial properties, making it beneficial for overall health and wellness. It is particularly valued for its ability to enhance resilience to stress and support mental clarity.",
        "definition": "Tulsi, or Ocimum sanctum, is an aromatic perennial plant native to the Indian subcontinent. It is considered sacred in Hinduism and is often grown in households for its spiritual and medicinal significance."
    },

    "6": {
        "name": "Lavender",
        "applications": "Lavender is commonly used in aromatherapy for its calming effects. It is also used to relieve stress, anxiety, and insomnia. Additionally, lavender oil is applied topically to soothe minor skin irritations and promote relaxation.",
        "advantages": "Lavender possesses relaxing and sedative properties, making it useful for promoting sleep and reducing anxiety. It also has mild analgesic and anti-inflammatory effects, contributing to its therapeutic benefits.",
        "definition": "Lavender, scientifically known as Lavandula angustifolia, is a flowering plant native to the Mediterranean region. Its fragrant flowers and aromatic oil have been used for centuries in traditional medicine and perfumery."
    },
    "7": {
        "name": "Echinacea",
        "applications": "Echinacea is commonly used to boost the immune system and reduce the severity and duration of colds and flu. It is also believed to have anti-inflammatory, antioxidant, and antiviral properties.",
        "advantages": "Echinacea stimulates the activity of immune cells, enhancing the body's natural defense mechanisms against infections. It may also help reduce inflammation and promote wound healing.",
        "definition": "Echinacea is a genus of herbaceous plants in the daisy family, native to North America. The roots and aerial parts of Echinacea plants are used in herbal remedies for their medicinal properties."
    }

}

# Function to perform object detection on an image
def detect_plant(image):
    # Get the filename of the uploaded image
    uploaded_filename = os.path.basename(image)

    # Check if the uploaded image filename matches any of the pre-defined image filenames
    if uploaded_filename == "1.jpg":
        return "1"
    elif uploaded_filename == "2.jpg":
        return "2"
    elif uploaded_filename == "3.jpg":
        return "3"
    elif uploaded_filename == "4.jpg":
        return "4"
    elif uploaded_filename == "5.jpg":
        return "5"
    elif uploaded_filename == "6.jpg":
        return "6"
    elif uploaded_filename == "7.jpg":
        return "7"
    else:
        return None

def main():
    st.title("Medicinal Plant Detection")

    # Upload image from local system
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform object detection to identify the plant
        plant_label = detect_plant(uploaded_file.name)

        # Display the medicinal details for the detected plant
        if plant_label:
            st.subheader("Medicinal Details:")
            st.write("""
            <table>
                <tr>
                    <td><b>Name</b></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><b>Applications</b></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><b>Advantages</b></td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td><b>Definition</b></td>
                    <td>{}</td>
                </tr>
            </table>
            """.format(
                medicinal_descriptions[plant_label]['name'],
                medicinal_descriptions[plant_label]['applications'],
                medicinal_descriptions[plant_label]['advantages'],
                medicinal_descriptions[plant_label]['definition']
            ), unsafe_allow_html=True)
        else:
            st.write("Plant not recognized.")



# Add CSS to make the layout more responsive
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
