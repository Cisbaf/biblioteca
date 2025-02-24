
function SearchFilter(e) {
    if (e && e.key != "Enter") {
        return
    }
    const input = document.getElementById("searchValue");
    AddParams('search', input.value);
}

function AddParams(filter_name, filter_value) {
    const params = new URLSearchParams(window.location.search);
    params.append(filter_name, filter_value)
    window.location.href = `${window.location.pathname}?${params.toString()}`;
}

function RemoveFilter(filter_name) {
    const params = new URLSearchParams(window.location.search);
    if (params.has(filter_name)) {
        params.delete(filter_name);  // Remove apenas o parâmetro específico
    }
    window.location.href = `${window.location.pathname}?${params.toString()}`;
}