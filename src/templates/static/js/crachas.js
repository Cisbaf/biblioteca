const datas = [
    {'id': 1, 'name': 'Daniel Fernandes Pereira', 'job': 'Engenheiro de Software', 'matricula': '2117897', 'cpf': '18714933748', 'rg': '287557672', 'model': {'name': 'cisbaf'}},
    {'id': 2, 'name': 'Ana Carolina Souza', 'job': 'Analista de Dados', 'matricula': '2117898', 'cpf': '25478963215', 'rg': '287557673', 'model': {'name': 'datainsights'}},
    {'id': 3, 'name': 'João Pedro Lima', 'job': 'Desenvolvedor Frontend', 'matricula': '2117899', 'cpf': '36541298745', 'rg': '287557674', 'model': {'name': 'webtech'}},
    {'id': 4, 'name': 'Mariana Duarte Alves', 'job': 'UX Designer', 'matricula': '2117900', 'cpf': '87451236985', 'rg': '287557675', 'model': {'name': 'designhub'}},
    {'id': 5, 'name': 'Carlos Henrique Silva', 'job': 'DevOps Engineer', 'matricula': '2117901', 'cpf': '96547812365', 'rg': '287557676', 'model': {'name': 'cloudops'}},
    {'id': 6, 'name': 'Fernanda Oliveira Castro', 'job': 'Product Manager', 'matricula': '2117902', 'cpf': '78459623147', 'rg': '287557677', 'model': {'name': 'prodmanage'}},
    {'id': 7, 'name': 'Rafael dos Santos', 'job': 'QA Engineer', 'matricula': '2117903', 'cpf': '63214598741', 'rg': '287557678', 'model': {'name': 'testlab'}},
    {'id': 8, 'name': 'Juliana Mendes Costa', 'job': 'Backend Developer', 'matricula': '2117904', 'cpf': '45871236987', 'rg': '287557679', 'model': {'name': 'servercore'}},
    {'id': 9, 'name': 'Fábio Gonçalves Ramos', 'job': 'Tech Lead', 'matricula': '2117905', 'cpf': '74125896325', 'rg': '287557680', 'model': {'name': 'leadtech'}},
    {'id': 10, 'name': 'Beatriz Lima Nunes', 'job': 'Data Scientist', 'matricula': '2117906', 'cpf': '32147859641', 'rg': '287557681', 'model': {'name': 'datasci'}},
    {'id': 11, 'name': 'Paulo Henrique Barbosa', 'job': 'Software Architect', 'matricula': '2117907', 'cpf': '63214587965', 'rg': '287557682', 'model': {'name': 'architech'}},
    {'id': 12, 'name': 'Carla Fernanda Duarte', 'job': 'Cybersecurity Analyst', 'matricula': '2117908', 'cpf': '85471236987', 'rg': '287557683', 'model': {'name': 'cybersecure'}},
    {'id': 13, 'name': 'Rodrigo Vasconcelos Martins', 'job': 'Full Stack Developer', 'matricula': '2117909', 'cpf': '96325814752', 'rg': '287557684', 'model': {'name': 'fullstacker'}},
    {'id': 14, 'name': 'Amanda Rocha Silveira', 'job': 'Marketing Digital', 'matricula': '2117910', 'cpf': '74185296354', 'rg': '287557685', 'model': {'name': 'marketguru'}},
    {'id': 15, 'name': 'Eduardo Tavares Silva', 'job': 'Scrum Master', 'matricula': '2117911', 'cpf': '65874123987', 'rg': '287557686', 'model': {'name': 'agileteam'}},
    {'id': 16, 'name': 'Natália Almeida Correia', 'job': 'Business Analyst', 'matricula': '2117912', 'cpf': '85412369741', 'rg': '287557687', 'model': {'name': 'bizanalyst'}},
    {'id': 17, 'name': 'Lucas Ferreira Monteiro', 'job': 'Engenheiro de Dados', 'matricula': '2117913', 'cpf': '32165498741', 'rg': '287557688', 'model': {'name': 'datengine'}},
    {'id': 18, 'name': 'Vanessa Ramos Costa', 'job': 'Suporte Técnico', 'matricula': '2117914', 'cpf': '98765412387', 'rg': '287557689', 'model': {'name': 'techsupport'}},
    {'id': 19, 'name': 'Gustavo Almeida Souza', 'job': 'Engenheiro de Machine Learning', 'matricula': '2117915', 'cpf': '74125896314', 'rg': '287557690', 'model': {'name': 'mlengine'}},
    {'id': 20, 'name': 'Isabela Mendes Rocha', 'job': 'Analista de Segurança', 'matricula': '2117916', 'cpf': '96385274156', 'rg': '287557691', 'model': {'name': 'secureanalyst'}}
];

function createTableRow(data) {
    const tr = document.createElement("tr");

    tr.innerHTML = `
        <td class="border-bottom-0">
            <div class="mb-3 form-check">
                <input id="${data.id}" name="checkboxs" type="checkbox" class="form-check-input" id="check${data.id}">
                <label class="form-check-label" for="check${data.id}">Selecionar</label>
            </div>
        </td>
        <td class="border-bottom-0">
            <h6 class="fw-semibold mb-1">${data.name}</h6>
            <span class="fw-normal">${data.job}</span>
        </td>
        <td class="border-bottom-0">
            <p class="mb-0 fw-normal">${data.model.name}</p>
        </td>
        <td class="border-bottom-0">
            <div class="d-flex align-items-center gap-2">
                <span class="badge bg-primary rounded-3 fw-semibold"></span>
            </div>
        </td>
    `;

    return tr;
}



function getData() {
    return new Promise(async(resolve, reject) => {
        const response = await fetch('/api')
    })
}



window.addEventListener("load", ()=>{
    table = new TableController("table-cracha", [' ', 'Colaborador', 'Modelo', 'Data'], datas, createTableRow);
    table.update();
});




function changeSelected(e) {
    console.log(e);
}



function addEventCheckBox() {
    const checkboxs = document.getElementsByName("checkboxs");
    for (let check of checkboxs) {
        check.addEventListener("change", changeSelected);
    }
}

