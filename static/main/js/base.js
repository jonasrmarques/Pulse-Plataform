document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggleSidebar');
    const content = document.querySelector('.content');
    
    // Adicionar title aos links para tooltip
    const sidebarLinks = sidebar.querySelectorAll('nav a');
    sidebarLinks.forEach(link => {
        const text = link.querySelector('.link-text').textContent;
        link.setAttribute('title', text);
    });
    
    // Verificar estado salvo no localStorage
    const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    
    if (isCollapsed) {
        sidebar.classList.add('collapsed');
    } else {
        sidebar.classList.remove('collapsed');
    }
    
    toggleBtn.addEventListener('click', function() {
        const isNowCollapsed = !sidebar.classList.contains('collapsed');
        sidebar.classList.toggle('collapsed');
        
        localStorage.setItem('sidebarCollapsed', isNowCollapsed);
        
        // Remover tooltip se estiver visível
        const activeTooltip = document.querySelector('nav a:hover::after');
        if (activeTooltip) {
            activeTooltip.style.display = 'none';
        }
    });
    
    // Ajustar para mobile
    function handleResponsive() {
        if (window.innerWidth < 768) {
            if (!sidebar.classList.contains('collapsed')) {
                sidebar.classList.add('collapsed');
                localStorage.setItem('sidebarCollapsed', 'true');
            }
        }
    }
    
    // Verificar na inicialização
    handleResponsive();
    
    // Ajustar ao redimensionar (com debounce)
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(handleResponsive, 250);
    });
});