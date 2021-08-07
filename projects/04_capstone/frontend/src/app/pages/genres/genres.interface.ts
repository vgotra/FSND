import { Genre } from "../genre/genre.interface";

export interface Genres {
    genres: Genre[];
    page: number;
    pages: number;
    total: number;
}