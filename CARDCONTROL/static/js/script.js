function runScript(event) {
    if (event.which == 13 || event.keyCode == 13) {
        var tb = document.getElementById("Enter");
        eval(tb.value);
        return false;
    }
    return true;
}