function addToCart() {
  const qty = document.getElementById("quantity").value;
  const coupon = document.getElementById("coupon").value;

  document.getElementById("message").innerText =
    "Book added to cart successfully!";
}

function fetchOrder(orderId) {
  return fetch(`${window.__BOOKHAVEN_CONFIG__.apiBase}/order?id=${orderId}`);
}

function getWishlist(userId) {
  return fetch(`${window.__BOOKHAVEN_CONFIG__.apiBase}/wishlist?user_id=${userId}`);
}

function updateUserRole(userId, role) {
  return fetch(`${window.__BOOKHAVEN_CONFIG__.apiBase}/user/role`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({user_id: userId, role: role})
  });
}

function getProfile(token) {
  return fetch(`${window.__BOOKHAVEN_CONFIG__.apiBase}/profile`, {
    headers: {'Authorization': `Bearer ${token}`}
  });
}

function getAdminReports() {
  return fetch(`${window.__BOOKHAVEN_CONFIG__.apiBase}/admin/reports`);
}
