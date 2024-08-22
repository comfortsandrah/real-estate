document.getElementById('filter-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const category = document.getElementById('category').value.toLowerCase();
    const location = document.getElementById('location').value.toLowerCase();
    const maxPrice = parseInt(document.getElementById('max-price').value, 10);

    const listings = document.querySelectorAll('.listing-item');
    let hasVisibleListings = false;

    listings.forEach(listing => {
        const listingCategory = listing.getAttribute('data-category').toLowerCase();
        const listingLocation = listing.getAttribute('data-location').toLowerCase();
        const listingPrice = parseInt(listing.getAttribute('data-price'), 10);

        let matchesCategory = !category || listingCategory === category;
        let matchesLocation = !location || listingLocation.includes(location);
        let matchesPrice = isNaN(maxPrice) || listingPrice <= maxPrice;

        if (matchesCategory && matchesLocation && matchesPrice) {
            listing.style.display = 'block';
            hasVisibleListings = true;
        } else {
            listing.style.display = 'none';
        }
    });

    document.getElementById('no-results-message').style.display = hasVisibleListings ? 'none' : 'block';
});

// Track visited listings
function markAsVisited(id) {
    const visitedListings = JSON.parse(localStorage.getItem('visitedListings')) || [];
    if (!visitedListings.includes(id)) {
        visitedListings.push(id);
        localStorage.setItem('visitedListings', JSON.stringify(visitedListings));
    }
}

// Check if a listing has been visited
function isVisited(id) {
    const visitedListings = JSON.parse(localStorage.getItem('visitedListings')) || [];
    return visitedListings.includes(id);
}

// Reset visited status when returning to listings
function resetVisitedStatus() {
    localStorage.removeItem('visitedListings');
}

// Call this function after booking is done to reset status
function onBookingSuccess() {
    setTimeout(() => {
        // Reset visited links and reload to listings
        resetVisitedStatus();
        window.location.href = 'listings.html'; // Change to your actual listings page URL
    }, 2000); // Wait for 2 seconds
}
// Call initializeLinkStates on page load
window.addEventListener('DOMContentLoaded', initializeLinkStates);
