function sessionVerifier() {
    var sessionExiste = sessionStorage.getItem('session') !== null;

    if (!sessionExiste) {
        window.location.href = '/login';
    }
}
sessionVerifier()