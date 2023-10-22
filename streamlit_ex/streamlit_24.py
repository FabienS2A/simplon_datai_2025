import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import scipy.stats
from scipy.stats import norm

st.title('Let\'s have some fun !! Youhou !!!!')

z_jpg = "https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg"
u_jpg = "https://upload.wikimedia.org/wikipedia/en/7/7b/Uncharted_2_box_artwork.jpg"
w_jpg = "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg"

tab1, tab2, tab3 = st.tabs(["The Fantastic Barr Graph", "The Lazy Circular Graph", "The Cerebral Surprise Graph"])

with tab1:
    st.header("A Gamer choice !!! Consoles once, consoles for life !! Okay, the witcher is more like a PC game...")
    st.write("Welcome in the world of Hyrule.\n You'll start a journey to save the princess and take the best on Ganon.\n Be care when you think you're close to the end, think BIGGER.\n The best game to start Adventure games and discover the Master Piece of this fabulous franchise. Enjoy")
    st.image(z_jpg, width=512)
    z = st.slider('Zelda 3, the king of 16 bits era ?', 0, 100, 50)
    st.write("Are you ready for a Non-Stop Action Game ! Did you think that the Indiana Jones franchise can have its first real competitor in a video game ? Trust me, when you get started, you'll never stop 'till the end !!!")
    st.image(u_jpg, width=512)
    u = st.slider('Uncharted 2, an unstopable Master piece which make PS3 a great console to have ?', 0, 100, 50)
    st.write("I can't explain the feeling of playing that game. Great story, Great characters, Great world... Get Geralt to its best adventure, while you discover the franchise with this episode or you already played the previous ones, it's not hours, it's days to go deep inside. I envy the ones who never played this game and can now start the journey. Be ready !!!")
    st.image(w_jpg, width=512)
    w = st.slider('The Witcher 3... No more words needed...', 0, 100, 50)
    
    st.write("And you ? Tell me what do you think about those games ?")
    
    x =  ['Zelda 3', 'Uncharted 2', 'The Witcher 3']
    y = [z, u, w]

    fig, ax = plt.subplots()

    games = ['Zelda 3', 'Uncharted 2', 'The Witcher 3']
    scores = [z, u, w]
    bar_colors = ['tab:green', 'tab:blue', 'tab:red']
    ax.bar(games, scores, color=bar_colors)
    ax.set_ylabel('score')
    ax.set_title('You\'re thinking')
    
    st.pyplot(fig)
   

with tab2:
    st.header("An Interactive Donut Graph !!! hmmmmm !! Donuts")
    st.write("The perfect recipe :")
    st.write("Sugar, the best drug ever :)")
    st.image("https://styleoga.it/wp-content/uploads/2023/03/come-sostituire-lo-zucchero.jpeg", width=512)
    x = st.text_input('label', placeholder = 'How much Sugar, miam.', label_visibility="hidden")
    st.write("Cream, What cows do the best, triple miam !!!")
    st.image("https://5.imimg.com/data5/SELLER/Default/2020/8/QR/VI/ZC/39237370/fresh-cow-milk-cream.jpg", width=512)
    y = st.text_input('label', placeholder = 'Volume of cream, be generous !!!', label_visibility="hidden")
    st.write("Chocolate, what else...")
    st.image("https://img.freepik.com/vecteurs-libre/illustration-journee-mondiale-du-chocolat-dessinee-main-barre-chocolat-muffin_23-2149429538.jpg", width=512)
    u = st.text_input('label', placeholder = 'Chocolate. Bammm !', label_visibility="hidden")
    st.write("That is a cake, not a fudge !!!")
    st.image("https://bakeitwithlove.com/wp-content/uploads/2022/06/How-To-Make-Bread-Flour-sq-500x500.jpg", width=512)
    z = st.text_input('label', placeholder = 'Flour, not too much...', label_visibility="hidden")
    st.write("Eggs, so cute !!!")
    st.image("https://ecoledesjuliettes.com/wp-content/uploads/2023/04/Poussin.jpg", width=512)
    w = st.text_input('label', placeholder = 'Nice pretty eggs.', label_visibility="hidden")
    
    

    if st.button('Cook it !!!'):
        data_frame = {'Sugar': int(x),
                'Cream': int(y),
                'Chocolate': int(u),
                'Flour': int(z),
                'Eggs': int(w)  }
        fig = px.pie(
        hole = .6,
        names = data_frame.keys(),
        values = data_frame.values(),
        color=data_frame.keys(),
        color_discrete_map= {'Sugar':'#C8AD7', 'Cream':'lightcyan','Chocolate':'chocolate','Flour':'antiquewhite','Eggs':'yellow'})
        st.header("Donut chart")
        st.plotly_chart(fig)
   

with tab3:
    st.header("A Surprise Graph...")
    
    down = st.slider('From Dumb', 40, 160, 90)
    up = st.slider('to Genuis', 40, 160, 110)

    x_min = 40.0
    x_max = 160.0

    mean = 100.0
    std = 15

    x = np.linspace(x_min, x_max, 1000)
    y = (scipy.stats.norm.pdf(x,mean,std))
    
    fig, ax = plt.subplots()
    ax.plot(x, y, color='black')
    ax.fill_between(x, y, where= (x>down) & (x<up), facecolor='cyan')
    st.pyplot(fig)
    
    cdf_upper_limit = norm(loc = 100 , scale = 15).cdf(up)
    cdf_lower_limit = norm(loc = 100 , scale = 15).cdf(down)
 
    prob = round(100*(cdf_upper_limit - cdf_lower_limit),1)
    st.write(str(prob), "percent of the population is in this range.")

    n = (up + down)/2

    if n <= 70 :
        st.image("https://www.challenges.fr/assets/img/2013/03/07/cover-r4x3w1200-578d30f668294-nan-mais-allo.png", width=512)
    elif n > 70 and n <= 90 :
        st.image("https://images.ladepeche.fr/api/v1/images/view/5c2e06d98fe56f0b27572b11/large/image.jpg", width=512)
    elif n > 90 and n <= 110 :
        st.image("https://m.media-amazon.com/images/I/516aiseZ-IL._AC_UF894,1000_QL80_.jpg", width=512)
    elif n > 110 and n <= 130 :
        st.image("https://nagalandpost.com/old_site/2018_8$large_illustration-.jpg", width=512)
    elif n > 130 and n <= 155 :
        st.image("https://www.curieux.live/wp-content/uploads/2023/05/smart-kid-in-glasses-having-idea-while-holding-dig-2022-12-16-19-17-17-utc-1.jpg", width=512)
    elif n > 155 :
        st.image("https://media.sudouest.fr/13298067/1200x-1/einstein-langue-1600-1600.jpg", width=512)