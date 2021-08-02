import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntityService } from "src/app/common/services/BaseStoreEntityService.service";
import { LanguageHttpService } from "./language.http.service";
import { Language } from "./language.interface";

@Injectable({ providedIn: 'root' })
export class LanguageStoreService extends BaseStoreEntityService<Language> {
    constructor(private service: LanguageHttpService) {
        super();
    }

    public LoadEntity(id: number): Observable<Language> {
        return this.service.getById(id).pipe(
            tap((response: Language) => this.set(response))
        );
    }
}