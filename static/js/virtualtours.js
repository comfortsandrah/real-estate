// Extract URL parameters
const urlParams = new URLSearchParams(window.location.search);
const propertyId = urlParams.get('propertyId');
const propertyName = urlParams.get('propertyName');

// Pre-fill the booking form with property details
if (propertyName) {
    document.getElementById('selected-property').innerText = propertyName;
    document.getElementById('property-id-input').value = propertyId;
}

// Handle form submission (example)
document.getElementById('booking-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Here you would typically handle form submission, e.g., send the data to a server
    alert(`Tour booked for ${propertyName} on ${document.getElementById('tour-date').value} at ${document.getElementById('tour-time').value}`);

    // Collect form data
    const email = document.getElementById('email').value;
    const tourDate = document.getElementById('tour-date').value;
    const tourTime = document.getElementById('tour-time').value;

     // Redirect to listings page after clicking "Okay"
     window.location.href = 'listings.html';

});
