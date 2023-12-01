document.addEventListener("DOMContentLoaded", function() {
    // Seu código JavaScript aqui
    $(document).ready(function() {
        $('.ver-detalhes-btn').click(function() {
            var modalId = $(this).data('target');
            $(modalId).modal('show');
        });
    });

    // Função para abrir o modal
    $(".reservar-btn").click(function () {
        // Mostrar o popup (substitua 'reservar-popup' pelo seletor real do seu popup)
        $("#reservar-popup").show();
    });

    // Fechar o popup ao clicar fora dele
    $(document).mouseup(function (e) {
        var container = $("#reservar-popup");
        if (!container.is(e.target) && container.has(e.target).length === 0) {
            container.hide();
        }
    });
});
