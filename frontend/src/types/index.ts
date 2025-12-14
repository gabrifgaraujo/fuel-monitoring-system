export interface Coleta {
    id: number;
    data_coleta: string;
    tipo_combustivel: string;
    volume_litros: number;
    preco_venda: number;
    cpf_motorista: string;
    cidade: string;
    tipo_veiculo: string;
    masked_cpf_motorista: string;
}

export interface KpiVolumeData {
    name: string;
    value: number;
}

export interface KpiEvolucaoData {
    date: string;
    price: number;
}

export interface FilterState {
    cidade: string;
    tipo_combustivel: string;
    data_inicio: string;
    data_fim: string;
}
