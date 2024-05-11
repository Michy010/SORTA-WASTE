// location.js

// Attach event listener to the link
document.getElementById('getLocationLink').addEventListener('click', function(event) {
    event.preventDefault();  // Prevent default link action

    // Call function to get user location
    getUserLocation();
});

// Function to get user location and send it to backend
function getUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;
                sendLocationToBackend(latitude, longitude);
            },
            function(error) {
                console.error('Error getting user location:', error);
            }
        );
    } else {
        console.error('Geolocation is not supported by this browser.');
    }
}

// Function to send location data to backend
function sendLocationToBackend(latitude, longitude) {
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var data = new URLSearchParams();
    data.append('latitude', latitude);
    data.append('longitude', longitude);
    data.append('csrfmiddlewaretoken', csrfToken);

    fetch('/update-location/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: data
    })
    .then(response => {
        if (response.ok) {
            console.log('Location data sent successfully.');
        } else {
            console.error('Failed to send location data:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error sending location data:', error);
    });
}
