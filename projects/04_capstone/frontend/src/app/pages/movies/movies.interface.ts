import { Movie } from "../movie/movie.interface";

export interface Movies {
    movies: Movie[];
    page: number;
    pages: number;
    total: number;
}