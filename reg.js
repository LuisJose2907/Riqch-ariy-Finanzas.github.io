const roleCards = document.querySelectorAll(".role-card");
let selectedRole = null;

roleCards.forEach((card) => {
  card.addEventListener("click", function () {
    roleCards.forEach((c) => c.classList.remove("active"));
    this.classList.add("active");
    selectedRole = this.dataset.role;
  });
});

// Indicador de fuerza de contraseña
const passwordInput = document.getElementById("password");
const strengthBar = document.querySelector(".password-strength-bar");

passwordInput.addEventListener("input", function () {
  const password = this.value;
  let strength = 0;

  if (password.length >= 8) strength += 25;
  if (password.match(/[a-z]+/)) strength += 25;
  if (password.match(/[A-Z]+/)) strength += 25;
  if (password.match(/[0-9]+/)) strength += 25;

  strengthBar.style.width = strength + "%";

  if (strength <= 25) {
    strengthBar.style.background = "#e74c3c";
  } else if (strength <= 50) {
    strengthBar.style.background = "#f39c12";
  } else if (strength <= 75) {
    strengthBar.style.background = "#f1c40f";
  } else {
    strengthBar.style.background = "#48bb78";
  }
});

// Manejo del formulario
const form = document.getElementById("registerForm");
form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (!selectedRole) {
    alert("Por favor, selecciona un tipo de usuario");
    return;
  }

  const formData = {
    role: selectedRole,
    nombre: document.getElementById("nombre").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    acceptedTerms: document.getElementById("terms").checked,
  };

  console.log("Datos del formulario:", formData);
  alert("¡Registro exitoso! (Esta es una demostración)");
});

// Botones sociales
const socialButtons = document.querySelectorAll(".btn-social");
socialButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const provider = this.textContent.trim();
    alert(`Registro con ${provider} (Esta es una demostración)`);
  });
});
