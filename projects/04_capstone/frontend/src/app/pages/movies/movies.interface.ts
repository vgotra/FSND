import { Entity } from "src/app/common/interfaces/Entity";

export interface Movie extends Entity {
    id: number;
    name: string;
    description: string;
    releaseDate: Date;
    releaseCountry: string;
}