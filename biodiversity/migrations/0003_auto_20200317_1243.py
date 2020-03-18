# Generated by Django 3.0.4 on 2020-03-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversity', '0002_auto_20200317_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gbif',
            name='abstract',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='acceptedNameUsageID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='acceptedScientificName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='accessRights',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='accrualMethod',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='accrualPeriodicity',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='accrualPolicy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='alternative',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='associatedOccurrences',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='associatedOrganisms',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='associatedReferences',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='associatedSequences',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='associatedTaxa',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='audience',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='available',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='basisOfRecord',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='bed',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='behavior',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='bibliographicCitation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='catalogNumber',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='collectionCode',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='collectionID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='conformsTo',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='continent',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='contributor',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='coordinatePrecision',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='countryCode',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='county',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='coverage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='created',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='creator',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dataGeneralizations',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='datasetID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='datasetKey',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='datasetName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='date',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dateAccepted',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dateCopyrighted',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dateIdentified',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dateSubmitted',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='depthAccuracy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='description',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='disposition',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='distanceAboveSurface',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='distanceAboveSurfaceAccuracy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='dynamicProperties',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='earliestAgeOrLowestStage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='earliestEonOrLowestEonothem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='earliestEpochOrLowestSeries',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='earliestEraOrLowestErathem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='earliestPeriodOrLowestSystem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='educationLevel',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='elevation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='elevationAccuracy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='establishmentMeans',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='eventDate',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='eventID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='eventRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='eventTime',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='extent',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='family',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='fieldNotes',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='fieldNumber',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='footprintSRS',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='footprintSpatialFit',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='footprintWKT',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='format',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='formation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='genericName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='genus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='geologicalContextID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='georeferenceProtocol',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='georeferenceRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='georeferenceSources',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='georeferenceVerificationStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='georeferencedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='group',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='habitat',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='hasCoordinate',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='hasFormat',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='hasGeospatialIssues',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='hasPart',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='hasVersion',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='higherClassification',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='higherGeography',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='higherGeographyID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='highestBiostratigraphicZone',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identificationID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identificationQualifier',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identificationReferences',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identificationRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identificationVerificationStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identifiedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='identifier',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='individualCount',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='informationWithheld',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='infraspecificEpithet',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='institutionCode',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='institutionID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='instructionalMethod',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isFormatOf',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isPartOf',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isReferencedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isReplacedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isRequiredBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='isVersionOf',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='island',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='islandGroup',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='issue',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='issued',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='kingdom',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='language',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lastCrawled',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lastInterpreted',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lastParsed',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='latestAgeOrHighestStage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='latestEonOrHighestEonothem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='latestEpochOrHighestSeries',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='latestEraOrHighestErathem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='latestPeriodOrHighestSystem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='license',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lifeStage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lithostratigraphicTerms',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='locality',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='locationAccordingTo',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='locationID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='locationRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='lowestBiostratigraphicZone',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='materialSampleID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='maximumDistanceAboveSurfaceInMeters',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='mediaType',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='mediator',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='medium',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='member',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='minimumDistanceAboveSurfaceInMeters',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='modified',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='municipality',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='nameAccordingTo',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='nameAccordingToID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='namePublishedIn',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='namePublishedInID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='namePublishedInYear',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='nomenclaturalCode',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='nomenclaturalStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='occurrenceID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='occurrenceRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='occurrenceStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='order',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismQuantity',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismQuantityType',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='organismScope',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='originalNameUsage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='originalNameUsageID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='otherCatalogNumbers',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='ownerInstitutionCode',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='parentEventID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='parentNameUsage',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='parentNameUsageID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='phylum',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='pointRadiusSpatialFit',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='preparations',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='previousIdentifications',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='protocol',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='provenance',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='publisher',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='publishingCountry',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='recordNumber',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='recordedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='references',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='relation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='relativeOrganismQuantity',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='repatriated',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='replaces',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='reproductiveCondition',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='requires',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='rights',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='rightsHolder',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='sampleSizeUnit',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='sampleSizeValue',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='samplingEffort',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='samplingProtocol',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='scientificName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='scientificNameID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='sex',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='source',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='spatial',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='species',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='specificEpithet',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='stateProvince',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='subgenus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='subgenusKey',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='subject',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='tableOfContents',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='taxonConceptID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='taxonID',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='taxonRank',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='taxonRemarks',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='taxonomicStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='temporal',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='title',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='type',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='typeStatus',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='typifiedName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='valid',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimCoordinateSystem',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimDepth',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimElevation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimEventDate',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimLocality',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimSRS',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimScientificName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='verbatimTaxonRank',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='vernacularName',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='gbif',
            name='waterBody',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
