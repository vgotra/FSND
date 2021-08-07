import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { Language } from "../language/language.interface";
import { LanguagesHttpService } from "./languages.http.service";
import { Languages } from "./languages.interface";

@Injectable({ providedIn: 'root' })
export class LanguagesStoreService extends BaseStoreEntitiesService<Language> {
    constructor(private service: LanguagesHttpService) {
        super();
    }

    public LoadEntities(): Observable<Languages> {
        return this.service.getAll().pipe(
            tap((response: Languages) => this.merge(response.languages))
        );
    }
}