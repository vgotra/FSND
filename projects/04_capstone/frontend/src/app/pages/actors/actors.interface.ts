import { Actor } from "../actor/actor.interface";

export interface Actors {
    actors: Actor[];
    page: number;
    pages: number;
    total: number;
}