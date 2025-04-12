import streamlit as st

# 🥤 Smoothie Builder App with Images
st.title("🍹 Build Your Own Smoothie!")
st.write("Pick your favorite fruits and we'll mix you a delicious smoothie!")

# Fruit data with images, calories, and fiber
fruits = {
    "Banana": {
        "image": "https://lacrosseallergy.com/wp-content/uploads/2024/05/bananas-whole-food.jpg",
        "calories": 105,
        "fiber": 3.1
    },
    "Strawberry": {
        "image": "https://extension.colostate.edu/wp-content/uploads/2021/04/07000-fig1.jpg",
        "calories": 50,
        "fiber": 2.0
    },
    "Mango": {
        "image": "https://blog2.pittmandavis.com/wp-content/uploads/2023/07/MangoFinal.jpg",
        "calories": 99,
        "fiber": 2.6
    },
    "Blueberry": {
        "image": "https://www.momjunction.com/wp-content/uploads/2016/12/8-Delightful-Health-Benefits-Of-Blueberries-For-Babies-1-1.jpg.webp",
        "calories": 84,
        "fiber": 3.6
    },
    "Pineapple": {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXsu8tZY65la03pHbvQtCiHg1ji_ybm3_bVlatNVJaLyyFuwvI-84ycH8t5iy7fkV3mKQ&usqp=CAU",
        "calories": 82,
        "fiber": 2.3
    },
    "Avocado": {
        "image": "https://images.immediate.co.uk/production/volatile/sites/30/2022/07/Avocado-sliced-in-half-ca9d808.jpg?quality=90&resize=440,400",
        "calories": 160,
        "fiber": 7.0
    },
}

# Multiselect for user fruit selection
selected_fruits = st.multiselect("Select Your Fruits:", list(fruits.keys()))

# Show smoothie details
if selected_fruits:
    st.subheader("🍹 Your Smoothie Ingredients:")

    total_calories = 0
    total_fiber = 0

    for fruit in selected_fruits:
        data = fruits[fruit]
        st.image(data["image"], width=250, caption=fruit)
        st.write(f"🔥 **Calories:** {data['calories']} kcal")
        st.write(f"🌿 **Fiber:** {data['fiber']} g")
        st.markdown("---")

        total_calories += data["calories"]
        total_fiber += data["fiber"]

    st.success(f"✅ **Total Calories:** {total_calories} kcal")
    st.info(f"🌿 **Total Fiber:** {total_fiber:.1f} g")

else:
    st.warning("👆 Select at least one fruit to build your smoothie!")
st.markdown("💡 Created with ❤️ using Streamlit")
