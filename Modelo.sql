CREATE TABLE publicacao.dwco_rbw
(
  type text,
  "right" text,
  "occurrenceID_GBIF" text,
  "rightsHolder" character varying(15),
  modified timestamp without time zone,
  "institutionCode" text,
  "collectionCode" character varying(15),
  "catalogNumber" text,
  "recordNumber" character varying,
  "recordedBy" text,
  "eventDate" text,
  year character varying(4),
  month character varying(2),
  day character varying(2),
  occurrenceremarks text,
  "fieldNotes" text,
  country character varying(120),
  "countryCode" character varying(2),
  "stateProvince" character varying(120),
  county character varying(120),
  locality text,
  "minimumElevationInMeters" character varying(20),
  "maximumElevationInMeters" character varying(20),
  "verbatimLatitude" text,
  "verbatimLongitude" text,
  "decimalLatitude" numeric,
  "decimalLongitude" numeric,
  "identifiedBy" text,
  "dateIdentified" text,
  "identificationRemarks" text,
  "identificationQualifier" text,
  "typeStatus" text,
  scientifname text,
  family text,
  genus text,
  "specificEpithet" text,
  "infraspecificEpithet" text,
  "taxonRank" text,
  "scientificNameAuthorship" character varying(150),
  "Clado" text,
  fieldnumber text,
  kingdom text,
  phylum text,
  "otherCatalogNumbers" text,
  "associatedMedia" text
)