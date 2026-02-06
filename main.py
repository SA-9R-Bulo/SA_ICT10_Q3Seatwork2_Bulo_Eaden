from pyscript import display, document
def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    section = document.getElementById('section').value

    if registration != 'registered':
        display('Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registration.', target='output')
    elif clearance != 'cleared':
        display('Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')
    elif section == '7 Emerald':
        display('Congratulations! You are part of the Cleveland Cavaliers', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://legacymedia.sportsplatform.io/img/images/photos/003/200/178/hi-res-9985c3a9dc6b9501bd41a74c71568272_crop_north.jpg?1418828901&w=630&h=420" style="height="auto" width="500px">'
    elif section == '7 Ruby':
        display('Congratulations! You are part of the Golden State Warriors', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://cdn.nba.com/manage/2017/12/GettyImages-684463444.jpg" style="height="auto" width="500px">'
    elif section == '8 Emerald':
        display('Congratulations! You are part of the Miami Heat', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5D1VZOQyNm7Ag7rekuiLzTwsJtShMMlSqHA&s" style="height="auto" width="500px">'
    elif section == '8 Ruby':
        display('Congratulations! You are part of the Los Angeles Lakers', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuhzkYWeuKSTzS4AEe6Vyja7ZyNwreJTrP2Q&s" style="height="auto" width="500px">'
    elif section == '9 Emerald':
        display('Congratulations! You are part of the Miami Heat', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5D1VZOQyNm7Ag7rekuiLzTwsJtShMMlSqHA&s" style="height="auto" width="500px">'
    elif section == '9 Ruby':
        display('Congratulations! You are part of the Los Angeles Lakers', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuhzkYWeuKSTzS4AEe6Vyja7ZyNwreJTrP2Q&s" style="height="auto" width="500px">'
    elif section == '10 Emerald':
        display('Congratulations! You are part of the Cleveland Cavaliers', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://legacymedia.sportsplatform.io/img/images/photos/003/200/178/hi-res-9985c3a9dc6b9501bd41a74c71568272_crop_north.jpg?1418828901&w=630&h=420" style="height="auto" width="400px">'
    elif section == '10 Ruby':
        display('Congratulations! You are part of the Golden State Warriors', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://cdn.nba.com/manage/2017/12/GettyImages-684463444.jpg" style="height="auto" width="500px">'