class TableController {
    constructor(table_id, columns, datas, lambda_data, page_items = 5) {
        this.table_id = table_id;
        this.columns = columns;
        this.datas = datas;
        this.lambda_data = lambda_data;
        this.page_items = page_items;
        this.page = 1;
        this.total_pages = Math.ceil(datas.length / page_items);
        
        this.element = document.getElementById(table_id);
        this.pagination = document.getElementById(`${table_id}-pagination`);
        
        this.render();
    }

    search_element(elements, condition) {
        return Array.from(elements).find(element => condition(element));
    }

    // Cria as colunas da tabela
    make_column() {
        const thead = this.search_element(this.element.childNodes, element => element.tagName === "THEAD");
        thead.appendChild(createColumns(this.columns));
    }

    // Renderiza os dados da página atual
    make_data(page) {
        const tbody = this.search_element(this.element.childNodes, element => element.tagName === "TBODY");
        tbody.innerHTML = ""; // Limpa os dados antigos
        const start = (page - 1) * this.page_items;
        const end = page * this.page_items;
        const pageData = this.datas.slice(start, end);

        pageData.forEach(data => {
            tbody.appendChild(this.lambda_data(data));
        });
    }

    // Cria os controles de paginação
    make_pagination() {
        const ul = this.search_element(this.pagination.childNodes, element => element.tagName === "UL");
        ul.innerHTML = ''; // Limpa os controles de paginação antigos
        ul.appendChild(createPage(this.total_pages, this.change_page.bind(this)));
    }

    // Atualiza a página de acordo com o número clicado
    change_page(pageNumber) {
        this.page = pageNumber;
        this.make_data(this.page);
        this.make_pagination();
    }

    // Função principal que renderiza a tabela
    render() {
        this.make_column();
        this.make_data(this.page);
        this.make_pagination();
    }

    // Função de busca (poderia ser estendida para buscar dados no array `datas`)
    search(query) {
        const filteredData = this.datas.filter(item => item.name.includes(query)); // Exemplo de busca
        this.datas = filteredData;
        this.total_pages = Math.ceil(filteredData.length / this.page_items);
        this.page = 1;
        this.render();
    }

    // Função para limpar a tabela
    clearTable() {
        const tbody = this.search_element(this.element.childNodes, element => element.tagName === "TBODY");
        tbody.innerHTML = "";
    }
}

// Função para criar as colunas
function createColumns(columns) {
    const tr = document.createElement("tr");
    columns.forEach(column => {
        const th = document.createElement("th");
        th.classList.add("border-bottom-0");
        const h6 = document.createElement("h6");
        h6.classList.add("fw-semibold", "mb-0");
        h6.textContent = column;
        th.appendChild(h6);
        tr.appendChild(th);
    });
    return tr;
}

// Função para criar a paginação
function createPage(count, lambda) {
    const ul = document.createElement('ul');
    ul.classList.add('pagination');

    const prevLi = document.createElement('li');
    prevLi.classList.add('page-item', 'disabled');
    const prevButton = document.createElement('button');
    prevButton.classList.add('page-link');
    prevButton.textContent = 'Previous';
    prevLi.appendChild(prevButton);
    ul.appendChild(prevLi);

    for (let x = 1; x <= count; x++) {
        const li = document.createElement('li');
        li.classList.add('page-item');
        const button = document.createElement('button');
        button.classList.add('page-link');
        button.textContent = x;
        button.addEventListener('click', () => lambda(x));
        li.appendChild(button);
        ul.appendChild(li);
    }

    const nextLi = document.createElement('li');
    nextLi.classList.add('page-item');
    const nextButton = document.createElement('a');
    nextButton.classList.add('page-link');
    nextButton.href = '#';
    nextButton.textContent = 'Next';
    nextLi.appendChild(nextButton);
    ul.appendChild(nextLi);

    return ul;
}

// Exemplo de função lambda para renderizar os dados da tabela
function renderData(data) {
    const tr = document.createElement("tr");
    Object.values(data).forEach(value => {
        const td = document.createElement("td");
        td.textContent = value;
        tr.appendChild(td);
    });
    return tr;
}
