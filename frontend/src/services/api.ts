import axios from 'axios';
import { Coleta, KpiVolumeData, KpiEvolucaoData, FilterState } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const fetchColetas = async (filters: FilterState, signal: AbortSignal): Promise<Coleta[]> => {
    const params = {
        cidade: filters.cidade || undefined,
        tipo_combustivel: filters.tipo_combustivel || undefined,
        data_inicio: filters.data_inicio || undefined,
        data_fim: filters.data_fim || undefined,
    };
    
    const response = await api.get<Coleta[]>('/coletas/', { params, signal });
    return response.data;
};

export const fetchKpiVolume = async (filters: FilterState, signal: AbortSignal): Promise<KpiVolumeData[]> => {
    const params = {
        cidade: filters.cidade || undefined,
        tipo_combustivel: filters.tipo_combustivel || undefined,
    };
    const response = await api.get<KpiVolumeData[]>('/kpi/volume-veiculo/', { params, signal });
    return response.data;
};

export const fetchKpiEvolucao = async (filters: FilterState, signal: AbortSignal): Promise<KpiEvolucaoData[]> => {
    const params = {
        cidade: filters.cidade || undefined,
        tipo_combustivel: filters.tipo_combustivel || undefined,
    };
    const response = await api.get<KpiEvolucaoData[]>('/kpi/evolucao-preco/', { params, signal });
    return response.data;
};
