import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { LanguagesHttpService } from "./languages.http.service";
import { Language } from "./languages.interface";

@Injectable({ providedIn: 'root' })
export class LanguagesStoreService extends BaseStoreEntitiesService<Language> {
    constructor(private service: LanguagesHttpService) {
        super();
    }

    public LoadEntities(): Observable<Language[]> {
        return this.service.getAll().pipe(
            tap((response: Language[]) => this.merge(response))
        );
    }
}