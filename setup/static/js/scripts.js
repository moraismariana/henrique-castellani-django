//PORTFOLIO
const botao = document.querySelector(".button");

function verMais() {
  const elementos = document.querySelectorAll(
    ".clientes-item:not(:nth-of-type(1),:nth-of-type(2),:nth-of-type(3),:nth-of-type(4))"
  );
  elementos.forEach((elemento) => {
    elemento.classList.toggle("vermais");
  });

  // Verificar se os elementos estão visíveis ou não e atualizar o texto do botão
  const algumElementoVisivel = Array.from(elementos).some(
    (elemento) => !elemento.classList.contains("vermais")
  );

  if (algumElementoVisivel) {
    botao.textContent = "ver mais";
  } else {
    botao.textContent = "ver menos";
  }
}

botao.addEventListener("click", verMais);

// MENU MOBILE
function menuShow() {
  let menuMobile = document.querySelector(".mobile-menu");
  let background = document.querySelector(
    ".mobile-menu-bg .background-overlay"
  );
  menuMobile.classList.toggle("none");
  background.classList.toggle("none");
}

document.querySelectorAll(".mobile-menu a").forEach((link) => {
  link.addEventListener("click", function () {
    menuShow();
  });
});
