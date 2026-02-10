const openBtn = document.querySelector('#show-dialog')
const closeBtn = document.querySelector('#close-dialog')
const modal = document.querySelector('#dialog')

openBtn && openBtn.addEventListener('click', () => {
  modal.showModal()
})

closeBtn && closeBtn.addEventListener('click', () => {
  modal.close()
})

const hamburger = document.querySelector('#hamburger')
const navMenu = document.querySelector('#nav-menu')
const menuOverlay = document.querySelector('#menu-overlay')

function toggleMenu() {
  hamburger.classList.toggle('active')
  navMenu.classList.toggle('active')
  menuOverlay.classList.toggle('active')

  document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : ''
}

hamburger && hamburger.addEventListener('click', toggleMenu)

menuOverlay && menuOverlay.addEventListener('click', toggleMenu)

const navLinks = document.querySelectorAll('.urls ul li a')

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (navMenu.classList.contains('active')) {
      toggleMenu()
    }
  })
})
