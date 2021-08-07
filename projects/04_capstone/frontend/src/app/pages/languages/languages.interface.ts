import { Language } from "../language/language.interface";

export interface Languages {
    languages: Language[];
    page: number;
    pages: number;
    total: number;
}