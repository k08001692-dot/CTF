
window.__BOOKHAVEN_CONFIG__ = {
  apiBase: "https://ctf-wego.onrender.com/api",
  theme: "pastel",
  currency: "INR",

  features: {
    couponsEnabled: true,
    wishlist: false,
    experimentalCheckout: true
  },

  endpoints: {
    books: "/books",
    book: "/book",
    login: "/login",
    checkout: "/checkout",
    status: "/status",
    order: "/order",
    wishlist: "/wishlist",
    profile: "/profile",
    userRole: "/user/role",
    adminReports: "/admin/reports"
  },

  debug: {
    enabled: false,
    build: "frontend-1.0.7",
    checksum: "a94a8fe5ccb19ba61c4c0873d391e987",
    testOrderId: 1002,
    testUserId: 2,
    meta: {
      reviewer: "qa-team",
      note_id: "FH-221",
      token_hint: "FLAG{frontend_whispers_secrets}"
    }
  }
};
