document.addEventListener('DOMContentLoaded', function() {
    const deletemodal = document.getElementById('DeletetaskModal');

    if (deletemodal) {
        deletemodal.addEventListener('show.bs.modal', function (event) {

            const button = event.relatedTarget;

           
            const taskTitle = button.getAttribute('data-task-title');
             const taskURL = button.getAttribute('data-url');

            const modalTitleSpan = deletemodal.querySelector('#TaskModal');
            const deleteform = deletemodal.querySelector('#DeletetaskModal');

            modalTitleSpan.textContent = taskTitle;

            deleteform.action = taskURL


        });    
    }
});