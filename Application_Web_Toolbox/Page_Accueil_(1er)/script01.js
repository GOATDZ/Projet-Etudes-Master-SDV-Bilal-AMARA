document.addEventListener('DOMContentLoaded', function() {
  // Démarrez l'animation du texte
  animateText();

  // Définissez une fonction pour l'animation du texte
  function animateText() {
    let dynamicText = document.querySelector('.dynamic-text');
    let text = "Bonjour et bienvenue dans \" LA TOOLBOX MASTER SDV \" !";
    let index = 0;

    function typeText() {
      if (index < text.length) {
        if (!dynamicText.querySelector('.cursor')) {
          dynamicText.insertAdjacentHTML('beforeend', '<span class="cursor"></span>');
        }
        dynamicText.textContent = text.substring(0, index + 1);
        index++;
        setTimeout(typeText, 120); // Ajustez la vitesse de l'animation du texte ici
      } else {
        // Masquez le curseur à la fin de l'animation
        document.querySelector('.cursor').style.opacity = '1'; // Assurez-vous que le curseur est visible à la fin
        animateCursor(); // Démarrez l'animation du curseur
        // Démarrez l'animation du bouton après l'animation du texte
        document.querySelector('.btn-animated').style.animationPlayState = 'running';
      }
    }

    setTimeout(typeText, 500); // Commencez à taper après un court délai
  }

  // Définissez une fonction pour l'animation continue du curseur
  function animateCursor() {
    let cursor = document.querySelector('.cursor');
    setInterval(function() {
      cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
    }, 500); // Changez la visibilité toutes les 500 ms pour créer le clignotement
  }
});


