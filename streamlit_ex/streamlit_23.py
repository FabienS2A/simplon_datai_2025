import streamlit as st

tab1, tab2, tab3 = st.tabs(["Adventure", "Action", "Both"])

with tab1:
   st.header("A Mervelous game")
   st.write("Welcome in the world of Hyrule.\n You'll start a journey to save the princess a take the best on Ganon.\n Be care when you think you're close to the end, think BIGGER.\n The best game to start Adventure game and discover the Master Piece of this fabulous franchise. Enjoy")
   st.image("https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg", width=512)

with tab2:
   st.header("A Tremendous game !")
   st.write("Are you ready for a Non-Stop Action Game ! Did you think that the Indiana Jones franchise can have its first real competitor in a video game ? Trust me, when you get started, you'll never stop 'till the end !!!")
   st.image("https://upload.wikimedia.org/wikipedia/en/7/7b/Uncharted_2_box_artwork.jpg", width=512)

with tab3:
   st.header("A perfect game !!!!")
   st.write("I can't explain the feeling of playing that game. Great story, Great characters, Great world... Get Gerald to its best adventure, while you discover the franchise with this episode or you already played the previous ones, it's not hours, it's days to go deep inside. I envy the ones who never played this game and can now start the journey. Be ready !!!")
   st.image("https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg", width=512)