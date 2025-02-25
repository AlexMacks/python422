console.log('Main.js loaded successfully!');

function goToPage(event) {
    event.preventDefault();
    
    const pageInput = document.getElementById('pageInput');
    const pageNumber = parseInt(pageInput.value);
    const maxPage = parseInt(pageInput.max);
    
    if (pageNumber && pageNumber > 0 && pageNumber <= maxPage) {
        // Получаем форму и добавляем номер страницы
        const form = document.getElementById('pageForm');
        const pageField = document.createElement('input');
        pageField.type = 'hidden';
        pageField.name = 'page';
        pageField.value = pageNumber;
        form.appendChild(pageField);
        
        // Отправляем форму
        form.submit();
    } else {
        alert(`Пожалуйста, введите число от 1 до ${maxPage}`);
    }
    return false;
}