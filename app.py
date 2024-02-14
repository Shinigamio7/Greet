import streamlit as st
import os
from pymongo import MongoClient


client = MongoClient(os.getenv('mongostr'), serverSelectionTimeoutMS=60000)
db = client['Experiment']
Records = db['Records']

def create_record(sender_name, reciever, receiver_crush):
    new_record = {
        "sender_name": sender_name,
        "receiver": reciever,
        "receiver_crush": receiver_crush
    }
    Records.insert_one(new_record)


def main():
    st.title('Greetings')
    
    zero, first, second, third, fourth, fifth, sixth, seventh, eighth = st.tabs(['Hey!','Rose Day', 'Propose Day', 'Chocolate Day', 'Teddy Day', 'Promise Day', 'Hug Day', 'Kiss Day', "Valentine's Day"])

    with zero:
        st.markdown("Share the link of the website whom you want to confess https://confess-your-feelings.streamlit.app/ ")
        sender_name = st.text_input("Who is confessing to you?")
        receiver = st.text_input("Who are you?")
        receiver_crush = st.text_input("If the person who sent, is not your crush? who do you want to send this to?")
        if st.button('Done!'):
            create_record(sender_name, receiver, receiver_crush)
            st.success('Done! 💌')
            if sender_name == receiver_crush:
                st.markdown(f'**{sender_name}** wanted to wish you, **{receiver}**. Please check the tabs to see the wishes. 🌹')

            else:
                st.markdown(f'Looks like you like {receiver_crush}** but **{sender_name}** wanted to wish you **{receiver}**. Please check the tabs  to see the wishes. 🌹')
    
    with first:
        if st.button('Click Me! 🌹'):
            st.markdown(''' > *Even a thousand Roses are no match to your beauty.*''') 
            st.markdown('''  Happy Rose Day! 🌹''')
            st.image('https://hd.wallpaperswide.com/thumbs/love_red_roses-t2.jpg', use_column_width=True)
    
    with second:
        if st.button('Click Me! 💖'):
            st.markdown(''' > *I adore you, I love you and I want only you for the rest of my life.*''') 
            st.markdown('''   Happy Propose Day! 💖''')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBKXJCbgtkD2TtX2SGkBcm_diZmnZcWeQdlA&usqp=CAU', use_column_width=True)
    
    with third:
        if st.button('Click Me! 🍫'):
            st.markdown(''' > *Thanks for entering my life and filling it with so much sweetness.*''') 
            st.markdown('''  Happy Chocolate Day! 🍫''')
            st.image('https://www.hdwallpapersfreedownload.com/uploads/large/special-days/happy-chocolate-day-heart-on-rose-petals-love-graphic-image-hd-wallpaper.jpg', use_column_width=True)
    
    with fourth:
        if st.button('Click Me! 🧸'):
            st.markdown(''' > *If you were  a Teddy, you would have been the cutest.*''') 
            st.markdown('''   Happy Teddy Day! 🧸''')
            st.image('https://c4.wallpaperflare.com/wallpaper/206/435/620/love-toy-heart-bear-wallpaper-preview.jpg', use_column_width=True)
    
    with fifth:
        if st.button('Click Me! 🤝'):
            st.markdown(''' > *I will love you more with each passing day.*''') 
            st.markdown('''   Happy Promise Day! 🤝''')
            st.image('https://wallpapers.com/images/hd/wandavision-pinky-promise-4k-09s6lysh02rrq666.jpg', use_column_width=True)
    
    with sixth:
        if st.button('Click Me! 🤗'):
            st.markdown(''' > *No medicine can heal me as much as your hug Does.*''') 
            st.markdown('''  Happy Hug Day! 🤗''')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYVHwAAuqC18-DgGrXyhJyoXyonaJfi63tTw&usqp=CAU', use_column_width=True)
    
    with seventh:
        if st.button('Click Me! ❤️'):
            st.markdown(''' > *The best things in life can never be kept, they must be given away, a smile, a kiss and love.*''') 
            st.markdown('''   Happy Kiss Day! ❤️''')
            st.image('https://c.ndtvimg.com/2021-02/t7g4l66_happy-kiss-day-kiss-day-images-kiss-day-quotes_625x300_12_February_21.jpg', use_column_width=True)
    
    with eighth:
        if st.button('Click Me! 💞'):
            st.markdown(''' > *You still make me laugh, you still give me butterflies and I am still falling for you.*''') 
            st.markdown('''  Happy Valentines  Day! 💞''')
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ66-UhsW_1B95O5c_3eWofNIs2i1ZZ0dFDZg&usqp=CAU', use_column_width=True)

if __name__ == '__main__':
    main()
