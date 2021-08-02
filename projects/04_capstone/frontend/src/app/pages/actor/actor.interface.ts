import { Entity } from "src/app/common/interfaces/Entity";

export interface Actor extends Entity {
    id: number;
    name: string;
    birthday: Date;
    sex: boolean;
    profileUrl: string;
    photoUrl: string;
}